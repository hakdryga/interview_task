*** Settings ***
Resource  common_keywords.robot
Suite Setup  API Test Setup
Suite Teardown  API Test Teardown

Test Template  Test API Template

*** Variables ***
${endpoint}  /planets


*** Test Cases ***
Test Planets With Id Greater Than 100   ${host_url}${endpoint}/101  404

Test Planets With Id Smaller Than 100   ${host_url}${endpoint}/12   200

Test Planets With Invalid Path          ${host_url}${endpoint}/     400

Test Planets With String Id             ${host_url}${endpoint}/ad   400

Test Planets With Negatative Id Value   ${host_url}${endpoint}/-3   400

Test Planets With Id Value 0            ${host_url}${endpoint}/0    404


