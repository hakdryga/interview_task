*** Settings ***
Resource  common_keywords.robot
Suite Setup  API Test Setup
Suite Teardown  API Test Teardown

Test Template  Test API Template

*** Variables ***
${endpoint}  /starships


*** Test Cases ***
Test Starships With Id Greater Than 100   ${host_url}${endpoint}/101    404

Test Starships With Id Equal 100          ${host_url}${endpoint}/100    200

Test Starships With Invalid Path          ${host_url}${endpoint}/       400

Test Starships With String Id             ${host_url}${endpoint}/star   400

Test Starships With Negatative Id Value   ${host_url}${endpoint}/-1     400

Test Starships With Id Value 0            ${host_url}${endpoint}/0      404
