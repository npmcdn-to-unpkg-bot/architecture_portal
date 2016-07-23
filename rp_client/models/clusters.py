# coding: utf-8

"""
    Resource provisioner API

    Provision Cloud Computing resources via API.

    OpenAPI spec version: 0.1.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Clusters(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Clusters - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'appliance': 'str',
            'uuid': 'str',
            'public_key': 'str',
            'user_id': 'int',
            'site_id': 'datetime',
            'master_node_id': 'int',
            'master_node_ip': 'str',
            'hosts_ips': 'list[str]',
            'hosts_ids': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'appliance': 'appliance',
            'uuid': 'uuid',
            'public_key': 'public_key',
            'user_id': 'user_id',
            'site_id': 'site_id',
            'master_node_id': 'master_node_id',
            'master_node_ip': 'master_node_ip',
            'hosts_ips': 'hosts_ips',
            'hosts_ids': 'hosts_ids'
        }

        self._id = None
        self._name = None
        self._appliance = None
        self._uuid = None
        self._public_key = None
        self._user_id = None
        self._site_id = None
        self._master_node_id = None
        self._master_node_ip = None
        self._hosts_ips = None
        self._hosts_ids = None

    @property
    def id(self):
        """
        Gets the id of this Clusters.
        Unique ID of the cluster

        :return: The id of this Clusters.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Clusters.
        Unique ID of the cluster

        :param id: The id of this Clusters.
        :type: int
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Clusters.
        Name given to the cluster

        :return: The name of this Clusters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Clusters.
        Name given to the cluster

        :param name: The name of this Clusters.
        :type: str
        """
        
        self._name = name

    @property
    def appliance(self):
        """
        Gets the appliance of this Clusters.
        Appliance of the cluster

        :return: The appliance of this Clusters.
        :rtype: str
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """
        Sets the appliance of this Clusters.
        Appliance of the cluster

        :param appliance: The appliance of this Clusters.
        :type: str
        """
        
        self._appliance = appliance

    @property
    def uuid(self):
        """
        Gets the uuid of this Clusters.
        Internal UUID given to the cluster

        :return: The uuid of this Clusters.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this Clusters.
        Internal UUID given to the cluster

        :param uuid: The uuid of this Clusters.
        :type: str
        """
        
        self._uuid = uuid

    @property
    def public_key(self):
        """
        Gets the public_key of this Clusters.
        Public key used to identify nodes of the cluster

        :return: The public_key of this Clusters.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this Clusters.
        Public key used to identify nodes of the cluster

        :param public_key: The public_key of this Clusters.
        :type: str
        """
        
        self._public_key = public_key

    @property
    def user_id(self):
        """
        Gets the user_id of this Clusters.
        ID of the user that created the cluster

        :return: The user_id of this Clusters.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Clusters.
        ID of the user that created the cluster

        :param user_id: The user_id of this Clusters.
        :type: int
        """
        
        self._user_id = user_id

    @property
    def site_id(self):
        """
        Gets the site_id of this Clusters.
        ID of the site in which nodes of the cluster are running

        :return: The site_id of this Clusters.
        :rtype: datetime
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """
        Sets the site_id of this Clusters.
        ID of the site in which nodes of the cluster are running

        :param site_id: The site_id of this Clusters.
        :type: datetime
        """
        
        self._site_id = site_id

    @property
    def master_node_id(self):
        """
        Gets the master_node_id of this Clusters.
        ID of the master node of the cluster (can be null)

        :return: The master_node_id of this Clusters.
        :rtype: int
        """
        return self._master_node_id

    @master_node_id.setter
    def master_node_id(self, master_node_id):
        """
        Sets the master_node_id of this Clusters.
        ID of the master node of the cluster (can be null)

        :param master_node_id: The master_node_id of this Clusters.
        :type: int
        """
        
        self._master_node_id = master_node_id

    @property
    def master_node_ip(self):
        """
        Gets the master_node_ip of this Clusters.
        IP address of the master node of the cluster (can be null)

        :return: The master_node_ip of this Clusters.
        :rtype: str
        """
        return self._master_node_ip

    @master_node_ip.setter
    def master_node_ip(self, master_node_ip):
        """
        Sets the master_node_ip of this Clusters.
        IP address of the master node of the cluster (can be null)

        :param master_node_ip: The master_node_ip of this Clusters.
        :type: str
        """
        
        self._master_node_ip = master_node_ip

    @property
    def appliance(self):
        """
        Gets the appliance of this Clusters.
        Appliance used (can be null)

        :return: The appliance of this Clusters.
        :rtype: str
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """
        Sets the appliance of this Clusters.
        Appliance used (can be null)

        :param appliance: The appliance of this Clusters.
        :type: str
        """
        
        self._appliance = appliance

    @property
    def hosts_ips(self):
        """
        Gets the hosts_ips of this Clusters.
        IP addresses of nodes of the cluster (can be null)

        :return: The hosts_ips of this Clusters.
        :rtype: list[str]
        """
        return self._hosts_ips

    @hosts_ips.setter
    def hosts_ips(self, hosts_ips):
        """
        Sets the hosts_ips of this Clusters.
        IP addresses of nodes of the cluster (can be null)

        :param hosts_ips: The hosts_ips of this Clusters.
        :type: list[str]
        """
        
        self._hosts_ips = hosts_ips

    @property
    def hosts_ids(self):
        """
        Gets the hosts_ids of this Clusters.
        IDs of nodes of the cluster (can be null)

        :return: The hosts_ids of this Clusters.
        :rtype: list[str]
        """
        return self._hosts_ids

    @hosts_ids.setter
    def hosts_ids(self, hosts_ids):
        """
        Sets the hosts_ids of this Clusters.
        IDs of nodes of the cluster (can be null)

        :param hosts_ids: The hosts_ids of this Clusters.
        :type: list[str]
        """
        
        self._hosts_ids = hosts_ids

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

