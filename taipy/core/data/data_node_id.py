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

from typing import Any, Dict, NewType

DataNodeId = NewType("DataNodeId", str)
"""Type that holds a `DataNode^` identifier."""
DataNodeId.__doc__ = """Type that holds a `DataNode^` identifier."""
Edit = NewType("Edit", Dict[str, Any])
"""Type that holds a `DataNode^` edit information."""
Edit.__doc__ = """Type that holds a `DataNode^` edit information."""
EDIT_TIMESTAMP_KEY = "timestamp"
EDIT_JOB_ID_KEY = "job_id"
EDIT_COMMENT_KEY = "comment"
EDIT_EDITOR_ID_KEY = "editor_id"
