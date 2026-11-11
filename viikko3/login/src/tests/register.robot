*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Registration Page

*** Test Cases ***

Register With Valid Username And Password
    Insert User  user1  user1234
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Insert User  u  user1234
    Registration Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Insert User  user2  u
    Registration Should Fail With Message  Password is too short

Register With Username That Is Already In Use
    Insert User  kalle  kalle123
    Registration Should Fail With Message  Username already in use

*** Keywords ***
Insert User
    [Arguments]    ${username}    ${password}
    Fill Text  id=username  ${username}
    Fill Text  id=password  ${password}
    Fill Text  id=password_confirmation  ${password}
    Click  button >> text=Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Registration Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Registration Page
    Reset Application
    Create User  kalle  kalle123
    Go To Registration Page