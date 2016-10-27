install-windowsfeature AD-domain-services
Import-Module ADDSDeployment
$pwd = ConvertTo-SecureString -String "Pa$$w0rd1234" -AsPlainText -Force
install-ADDSForest -DomainName "testDomain.strikertech.com" -DomainMode 6 -Force -ForestMode 6 -SafeModeAdministratorPassword $pwd 