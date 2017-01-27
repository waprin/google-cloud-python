# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Interact with Stackdriver Error Reporting via Logging API.

It's possible to report Stackdriver Error Reporting errors by formatting
structured log messages in Stackdriver Logging in a given format. This
client provides a mechanism to report errors using that technique.
"""

import google.cloud.logging.client


class _ErrorReportingLoggingAPI(object):
    """Report to Stackdriver Error Reporting via Logging API"""
    def __init__(self, project, credentials=None, http=None):
        self.logging_client = google.cloud.logging.client.Client(
            project, credentials, http)

    def report_error_event(self, error_report):
        """Report error payload.

        :type error_report: dict
        :param: error_report:
            dict payload of the error report formatted according to
            https://cloud.google.com/error-reporting/docs/formatting-error-messages
            This object should be built using
            :meth:~`google.cloud.error_reporting.client._build_error_report`
        """
        logger = self.logging_client.logger('errors')
        logger.log_struct(error_report)
