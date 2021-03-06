# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging

from horizon import api
from horizon import tables
from .tables import ServicesTable


LOG = logging.getLogger(__name__)


class IndexView(tables.DataTableView):
    table_class = ServicesTable
    template_name = 'syspanel/services/index.html'

    def get_data(self):
        services = []
        for i, service in enumerate(self.request.user.service_catalog):
            service['id'] = i
            services.append(api.keystone.Service(service))
        return services
