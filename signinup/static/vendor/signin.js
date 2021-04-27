AWSCognito.config.region = CognitoConfig.region;

var poolData = {
    UserPoolId: CognitoConfig.userPoolId,
    ClientId: CognitoConfig.appClientId
};

var userPool = new AWSCognito.CognitoIdentityServiceProvider.CognitoUserPool(poolData);

var cognitoUser;

function submitSignin() {
    // 입력 폼에서 ID와 비밀번호를 입력받습니다.
    // 저는 phone number를 alias로 설정해서 ID 처럼 사용할 수 있게 했습니다.
    var user_PhoneNumber = document.getElementById("signin_phonenumber").value;
    var user_Pw = document.getElementById("signin_pwd").value;

    // ID와 Password를 정해진 속성명인 Username과 Password에 담습니다.
    var authenticationData = {
        Username: user_PhoneNumber,
        Password: user_Pw
    };

    // 여기에는 ID와 User Pool 정보를 담아 놓습니다.
    var userData = {
        Username: user_PhoneNumber, // your username here
        Pool: userPool
    };

    // 로그인을 위해 Cognito 객체 2개를 준비합니다.
    var authenticationDetails = new AWSCognito.CognitoIdentityServiceProvider.AuthenticationDetails(authenticationData);
    var cognitoSignedUser = new AWSCognito.CognitoIdentityServiceProvider.CognitoUser(userData);

    // authenticateUser 함수로 로그인을 시도합니다.
    cognitoSignedUser.authenticateUser(authenticationDetails, {
        onSuccess: function(result) {
            // 로그인에 성공하면 Token이 반환되어 옵니다.
            console.log('access token + ' + result.getAccessToken().getJwtToken());
            // API Gateway로 만든 API에 Request를 보낼 때는 Authorization 헤더의 값으로 idToken을 넣어야합니다.
            console.log('idToken + ' + result.idToken.jwtToken);
        },
        onFailure: function(err) {
            alert(err);
        }
    });
}