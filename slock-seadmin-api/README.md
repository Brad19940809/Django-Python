# Project Slock - Security Admin System
## API List
### Registration
#### Method
POST

#### URL
auth/register/

#### Input
- `username` 用户名，0-10 的数字
- `password` 密码，这里有一些说明，不能为空

#### Output
None

#### Status Code
- `201` 创建成功

#### Comments
c 和 d 必须与 a 和 b 对应，具体算法：a+sdkajflkasd

#### Example
`http://192.168.71.220/api/slock/auth/register/`
```
{
username: sfdsafds,
password: dsalfkjdsl,
two_level: {}
    a: 'b'
}
```
```
{sdlkafjdlsafj}
```
### Log In
