#!/usr/bin/env python3
import unittest
import kubeconfig_plugin
from arcaflow_plugin_sdk import plugin


class KubeconfigPluginTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            kubeconfig_plugin.InputParams(
                "kubeconfig: apiVersion: v1clusters:   - cluster:   certificate-authority-data:"
            )
        )

        plugin.test_object_serialization(
            kubeconfig_plugin.kubeconfig_output_schema.unserialize(
                {
                    "cluster_name": "arcaflow",
                    "server_url": "https://api.arcaflow.cluster.openshift.com:6443",
                    "certificate_authority_data": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSU",
                    "user": "admin",
                    "client_certificate_data": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FUUNBVEUtLS0tLQo=",
                    "client_key_data": "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcEF",
                }
            )
        )

        plugin.test_object_serialization(
            kubeconfig_plugin.ErrorOutput(
                exit_code=1, error="This is an error"
            )
        )


if __name__ == "__main__":
    unittest.main()
