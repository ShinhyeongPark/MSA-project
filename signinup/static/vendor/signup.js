AWSCognito.config.region = CognitoConfig.region;

var poolData = {
    UserPoolId: CognitoConfig.userPoolId,
    ClientId: CognitoConfig.appClientId
};

var userPool = new AWSCognito.CognitoIdentityServiceProvider.CognitoUserPool(poolData);

var cognitoUser;

function submitSignUp() {
    // 가입할 때 사용자가 입력한 정보들을 저장할 배열입니다.
    var attributeList = [];

    // 입력 폼에서 입력된 값을 받아오는 부분입니다. 일반적인 javascript입니다.
    var user_Name = document.getElementById("signup_username").value;
    var user_PhoneNumber = document.getElementById("signup_phonenumber").value;
    var user_Pw = document.getElementById("signup_pwd").value;
    console.log('user data : ', user_Name, ', ', user_PhoneNumber, ', ', user_Pw);

    // 이 변수가 사용자가 입력한 정보 중 하나를 입력하는 변수입니다.
    // 저는 핸드폰 번호만 입력받았습니다.
    // 변수명은 자유롭게 사용가능하나, Name은 AWS Cognito에서 정해주는대로 써야합니다.
    // 목록 : address, birthdate, email, family_name, gender, given_name, locale
    //   , middle_name, name, nickname, phone_number, picture, preferred_username
    //   , profile, timezone, updated_at, website
    var dataPhoneNumber = {
        Name: 'phone_number',
        Value: user_PhoneNumber
    };

    // Attribute를 AWS Cognito가 알아들을 수 있는 객체로 만듭니다.
    var attributePhoneNumber = new AWSCognito.CognitoIdentityServiceProvider.CognitoUserAttribute(dataPhoneNumber);

    // 방금 위에서 만든 Attribute 객체를 Attribute List에 추가시킵니다.
    // 이렇게 배열에 다 추가시키고 한번에 Cognito에 넘길겁니다.
    attributeList.push(attributePhoneNumber);

    // 전역변수로 만들어 놓은 User Pool 객체에서는 signup 함수를 제공합니다.
    // 인자는 User name(ID 인것 같네요.), Password, Attribute List, null(무슨 자리인지 모르겠어요..확인해야합니다.ㅎㅎ), 처리 결과가 오면 수행 될 callback 함수 입니다.
    userPool.signUp(user_Name, user_Pw, attributeList, null, function(err, result) {
        if (err) {
            // error가 발생하면 여기로 빠집니다.
            alert(err);
            return;
        }

        // 가입이 성공하면 result에 가입된 User의 정보가 되돌아 옵니다.
        // 인증 함수에서 사용해야하기에 위에서 만든 전역변수인 cognitoUser에 넣어놓습니다.
        cognitoUser = result.user;
        console.log('user name is ' + cognitoUser.getUsername());
    });
}