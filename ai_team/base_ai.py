

# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2025 HANNAHANAHANNAH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.


class BaseAi:
    def __init__(self, name, role, system_prompt, memory_path, model):
        self.name = name
        self.role = role
        self.system_prompt = system_prompt
        self.memory_path = memory_path
        self.model = model

