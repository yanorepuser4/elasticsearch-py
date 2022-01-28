#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from typing import Any, Dict, List, Optional, Union

from elastic_transport import ObjectApiResponse

from ._base import NamespacedClient
from .utils import SKIP_IN_PATH, _quote, _rewrite_parameters


class SqlClient(NamespacedClient):
    @_rewrite_parameters(
        body_fields=True,
    )
    def clear_cursor(
        self,
        *,
        cursor: str,
        error_trace: Optional[bool] = None,
        filter_path: Optional[Union[List[str], str]] = None,
        human: Optional[bool] = None,
        pretty: Optional[bool] = None,
    ) -> ObjectApiResponse[Any]:
        """
        Clears the SQL cursor

        `<https://www.elastic.co/guide/en/elasticsearch/reference/current/clear-sql-cursor-api.html>`_

        :param cursor:
        """
        if cursor is None:
            raise ValueError("Empty value passed for parameter 'cursor'")
        __path = "/_sql/close"
        __body: Dict[str, Any] = {}
        __query: Dict[str, Any] = {}
        if cursor is not None:
            __body["cursor"] = cursor
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST", __path, params=__query, headers=__headers, body=__body
        )

    @_rewrite_parameters()
    def delete_async(
        self,
        *,
        id: Any,
        error_trace: Optional[bool] = None,
        filter_path: Optional[Union[List[str], str]] = None,
        human: Optional[bool] = None,
        pretty: Optional[bool] = None,
    ) -> ObjectApiResponse[Any]:
        """
        Deletes an async SQL search or a stored synchronous SQL search. If the search
        is still running, the API cancels it.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/delete-async-sql-search-api.html>`_

        :param id: The async search ID
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path = f"/_sql/async/delete/{_quote(id)}"
        __query: Dict[str, Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    def get_async(
        self,
        *,
        id: Any,
        delimiter: Optional[str] = None,
        error_trace: Optional[bool] = None,
        filter_path: Optional[Union[List[str], str]] = None,
        format: Optional[str] = None,
        human: Optional[bool] = None,
        keep_alive: Optional[Any] = None,
        pretty: Optional[bool] = None,
        wait_for_completion_timeout: Optional[Any] = None,
    ) -> ObjectApiResponse[Any]:
        """
        Returns the current status and available results for an async SQL search or stored
        synchronous SQL search

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/get-async-sql-search-api.html>`_

        :param id: The async search ID
        :param delimiter: Separator for CSV results. The API only supports this parameter
            for CSV responses.
        :param format: Format for the response. You must specify a format using this
            parameter or the Accept HTTP header. If you specify both, the API uses this
            parameter.
        :param keep_alive: Retention period for the search and its results. Defaults
            to the `keep_alive` period for the original SQL search.
        :param wait_for_completion_timeout: Period to wait for complete results. Defaults
            to no timeout, meaning the request waits for complete search results.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path = f"/_sql/async/{_quote(id)}"
        __query: Dict[str, Any] = {}
        if delimiter is not None:
            __query["delimiter"] = delimiter
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if human is not None:
            __query["human"] = human
        if keep_alive is not None:
            __query["keep_alive"] = keep_alive
        if pretty is not None:
            __query["pretty"] = pretty
        if wait_for_completion_timeout is not None:
            __query["wait_for_completion_timeout"] = wait_for_completion_timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    def get_async_status(
        self,
        *,
        id: Any,
        error_trace: Optional[bool] = None,
        filter_path: Optional[Union[List[str], str]] = None,
        human: Optional[bool] = None,
        pretty: Optional[bool] = None,
    ) -> ObjectApiResponse[Any]:
        """
        Returns the current status of an async SQL search or a stored synchronous SQL
        search

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/get-async-sql-search-status-api.html>`_

        :param id: The async search ID
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path = f"/_sql/async/status/{_quote(id)}"
        __query: Dict[str, Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters(
        body_fields=True,
        ignore_deprecated_options={"request_timeout"},
    )
    def query(
        self,
        *,
        columnar: Optional[bool] = None,
        cursor: Optional[str] = None,
        error_trace: Optional[bool] = None,
        fetch_size: Optional[int] = None,
        field_multi_value_leniency: Optional[bool] = None,
        filter: Optional[Any] = None,
        filter_path: Optional[Union[List[str], str]] = None,
        format: Optional[str] = None,
        human: Optional[bool] = None,
        page_timeout: Optional[Any] = None,
        pretty: Optional[bool] = None,
        query: Optional[str] = None,
        request_timeout: Optional[Any] = None,
        time_zone: Optional[str] = None,
    ) -> ObjectApiResponse[Any]:
        """
        Executes a SQL request

        `<https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-search-api.html>`_

        :param columnar:
        :param cursor:
        :param fetch_size: The maximum number of rows (or entries) to return in one response
        :param field_multi_value_leniency: Throw an exception when encountering multiple
            values for a field (default) or be lenient and return the first value from
            the list (without any guarantees of what that will be - typically the first
            in natural ascending order).
        :param filter: Optional Elasticsearch query DSL for additional filtering.
        :param format: a short version of the Accept header, e.g. json, yaml
        :param page_timeout: The timeout before a pagination request fails.
        :param query: SQL query to execute
        :param request_timeout: The timeout before the request fails.
        :param time_zone: Time-zone in ISO 8601 used for executing the query on the server.
            More information available here.
        """
        __path = "/_sql"
        __body: Dict[str, Any] = {}
        __query: Dict[str, Any] = {}
        if columnar is not None:
            __body["columnar"] = columnar
        if cursor is not None:
            __body["cursor"] = cursor
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if fetch_size is not None:
            __body["fetch_size"] = fetch_size
        if field_multi_value_leniency is not None:
            __body["field_multi_value_leniency"] = field_multi_value_leniency
        if filter is not None:
            __body["filter"] = filter
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if human is not None:
            __query["human"] = human
        if page_timeout is not None:
            __body["page_timeout"] = page_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if query is not None:
            __body["query"] = query
        if request_timeout is not None:
            __body["request_timeout"] = request_timeout
        if time_zone is not None:
            __body["time_zone"] = time_zone
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST", __path, params=__query, headers=__headers, body=__body
        )

    @_rewrite_parameters(
        body_fields=True,
    )
    def translate(
        self,
        *,
        query: str,
        error_trace: Optional[bool] = None,
        fetch_size: Optional[int] = None,
        filter: Optional[Any] = None,
        filter_path: Optional[Union[List[str], str]] = None,
        human: Optional[bool] = None,
        pretty: Optional[bool] = None,
        time_zone: Optional[str] = None,
    ) -> ObjectApiResponse[Any]:
        """
        Translates SQL into Elasticsearch queries

        `<https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-translate-api.html>`_

        :param query:
        :param fetch_size:
        :param filter:
        :param time_zone:
        """
        if query is None:
            raise ValueError("Empty value passed for parameter 'query'")
        __path = "/_sql/translate"
        __body: Dict[str, Any] = {}
        __query: Dict[str, Any] = {}
        if query is not None:
            __body["query"] = query
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if fetch_size is not None:
            __body["fetch_size"] = fetch_size
        if filter is not None:
            __body["filter"] = filter
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if time_zone is not None:
            __body["time_zone"] = time_zone
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST", __path, params=__query, headers=__headers, body=__body
        )
