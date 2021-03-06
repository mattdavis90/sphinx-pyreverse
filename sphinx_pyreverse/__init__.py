'''
Created on Oct 1, 2012

@author: alendit
'''
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive
from subprocess import call
import os

try:
    from PIL import Image as IMAGE
except ImportError, error:
    IMAGE = None

# debugging with IPython
#try:
#    from IPython import embed
#except ImportError, e:
#    pass


class UMLGenerateDirective(Directive):
    """UML directive to generate a pyreverse diagram"""
    required_arguments = 1
    optional_arguments = 0
    has_content = False
    DIR_NAME = "uml_images"

    def run(self):
        env = self.state.document.settings.env
        src_dir = env.srcdir
        doc_dir = os.path.dirname(env.docname)
        uml_dir = os.path.join(src_dir, doc_dir, self.DIR_NAME)

        if os.path.basename(uml_dir) not in os.listdir(os.path.join(src_dir, doc_dir)):
            os.mkdir(uml_dir)

        env.uml_dir = uml_dir

        module_path = os.path.abspath(self.arguments[0])
        module_dir = os.path.abspath(os.path.join(src_dir, module_path))

        basename = os.path.basename(module_path).split(".")[0]
        classes_img = "classes_{0}.png".format(basename)
        packages_img = "packages_{0}.png".format(basename)

        os.chdir(module_dir)

        print call(['pyreverse', '-o', 'png', '-p', basename, module_dir])

        os.rename(classes_img, os.path.join(uml_dir, classes_img))
        try:
            os.remove(packages_img)
        except:
            print "Could not find", packages_img

        max_width = 1000
        img_width = 1000

        if IMAGE:
            i = IMAGE.open(os.path.join(uml_dir, classes_img))
            
            if i.size[0] < max_width:
                img_width = i.size[0]

        uri = directives.uri(os.path.join(self.DIR_NAME, classes_img))
        img = nodes.image(uri=uri, width=str(img_width))

        os.chdir(src_dir)

        return [img]


def setup(app):
    """Setup directive"""
    app.add_directive('uml', UMLGenerateDirective)
