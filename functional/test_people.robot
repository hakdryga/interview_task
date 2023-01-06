*** Settings ***
Resource  ./resources/common_keywords.robot
Suite Setup  API Test Setup
Suite Teardown  API Test Teardown

Test Template  Test API Template

*** Variables ***
${endpoint}  /people


*** Test Cases ***
Test People With Id Greater Than 100   ${host_url}${endpoint}/101    404

Test People With Id Equal 100          ${host_url}${endpoint}/100    200

Test People With Invalid Path          ${host_url}${endpoint}/       400

Test People With String Id             ${host_url}${endpoint}/peop   400

Test People With Negatative Id Value   ${host_url}${endpoint}/-10    400

Test People With Id Value 0            ${host_url}${endpoint}/0      404