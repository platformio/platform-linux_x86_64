# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from platformio.public import PlatformBase
from platformio.util import get_systype


class Linux_x86_64Platform(PlatformBase):

    @property
    def packages(self):
        packages = PlatformBase.packages.fget(self)
        if (get_systype() == "linux_x86_64" and
                "toolchain-gcclinux64" in packages):
            del packages['toolchain-gcclinux64']
        return packages
