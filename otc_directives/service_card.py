# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import yaml

from docutils import nodes

from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective


LOG = logging.getLogger(__name__)


class service_card(nodes.General, nodes.Element):
    pass


class ServiceCard(SphinxDirective):
    node_class = service_card
    option_spec = {
        # 'service_type': directives.unchanged_required,
    }

    has_content = False

    def run(self):
        node = self.node_class()
        # node['service_type'] = self.options.get('service_type')
        return [node]

def service_card_html(self, node):
    # This method renders containers per each service of the category with all
    # links as individual list items
    data = '''
        <div class="card">
        <h5 class="card-header">Featured</h5>
        <div class="card-body">
        <h5 class="card-title">Special title treatment</h5>
        <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
        </div>'''
    self.body.append(data)
    raise nodes.SkipNode

def setup(app):
    app.add_node(service_card,
                 html=(service_card_html, None))
    app.add_directive("service_card", ServiceCard)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
