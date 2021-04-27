AWSCognito.config.region = CognitoConfig.region;

var poolData = {
    UserPoolId: CognitoConfig.userPoolId,
    ClientId: CognitoConfig.appClientId
};

var userPool = new AWSCognito.CognitoIdentityServiceProvider.CognitoUserPool(poolData);

var cognitoUser;

function submitActivateCode() {
    // 회원가입을 하면 User Pool을 어떻게 만들었냐에 따라서 email 또는 phone으로 인증코드가 발송됩니다.
    // 사용자로부터 인증코드를 입력받아옵니다.
    var user_activatecode = document.getElementById("activate_code").value;

    // cognitoUser는 가입함수에서 가입 성공 후 되돌아온 사용자 정보가 담겨있습니다.
    // 이 변수에서 바로 confirmRegistration함수를 수행하면 AWS Cognito로 인증 요청을 합니다.
    // 인자는 인증코드, true(이것도 알아봐야합니다..ㅎㅎ), callback 함수 입니다.
    cognitoUser.confirmRegistration(user_activatecode, true, function(err, result) {
        if (err) {
            alert(err);
            return;
        }
        // 인증이 성공하면 SUCCESS 문자가 되돌아 옵니다.
        console.log('call result : ' + result);
    });
}