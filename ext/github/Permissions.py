# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from __future__ import absolute_import

import github.GithubObject


class Permissions(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Permissions
    """

    def __repr__(self):
        return self.get__repr__(
            {
                "admin": self._admin.value,
                "pull": self._pull.value,
                "push": self._push.value,
            }
        )

    @property
    def admin(self):
        """
        :type: bool
        """
        return self._admin.value

    @property
    def pull(self):
        """
        :type: bool
        """
        return self._pull.value

    @property
    def push(self):
        """
        :type: bool
        """
        return self._push.value

    def _initAttributes(self):
        self._admin = github.GithubObject.NotSet
        self._pull = github.GithubObject.NotSet
        self._push = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "admin" in attributes:  # pragma no branch
            self._admin = self._makeBoolAttribute(attributes["admin"])
        if "pull" in attributes:  # pragma no branch
            self._pull = self._makeBoolAttribute(attributes["pull"])
        if "push" in attributes:  # pragma no branch
            self._push = self._makeBoolAttribute(attributes["push"])
