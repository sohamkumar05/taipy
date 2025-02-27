# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
# -----------------------------------------------------------------------------------------
# To execute this script, make sure that the taipy-gui package is installed in your
# Python environment and run:
#     python <script>
# -----------------------------------------------------------------------------------------
import datetime

from taipy.gui import Gui

start_date = datetime.datetime(2023, 3, 26, 7, 37)
end_date   = datetime.datetime(2023, 3, 26, 19, 2)
dates = [start_date, end_date]

# Note: |analogic| option only take effect if you put |with_time| before it
page = "<|{dates}|date_range|with_time|analogic|>"

if __name__ == "__main__":
    Gui(page).run(title="Date Range - With time")
