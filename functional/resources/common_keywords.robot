*** Settings ***
Library  Process
Library  RequestsLibrary

*** Variables ***
${server_process_alias}     simple_server
${host_ip}                  localhost
${host_port}                8030
${host_url}                 http://${host_ip}:${host_port}


*** Keywords ***

API Test Setup
    ${process}=  Start Process  python  ../common/run_server.py  -h  ${host_ip}  -p  ${host_port}  alias=${server_process_alias}
    Wait For Process  ${server_process_alias}  timeout=3 sec

API Test Teardown
    Terminate Process  ${server_process_alias}

Test API Template
    [Arguments]  ${url}  ${expected_status}
    ${response}  GET  ${url}  expected_status=anything
    Status Should Be  ${expected_status}