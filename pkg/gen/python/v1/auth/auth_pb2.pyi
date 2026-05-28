from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResetPasswordRequest(_message.Message):
    __slots__ = ("email", "reset_code", "new_password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    RESET_CODE_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    reset_code: str
    new_password: str
    def __init__(self, email: _Optional[str] = ..., reset_code: _Optional[str] = ..., new_password: _Optional[str] = ...) -> None: ...

class ResetPasswordResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class ResendVerifyCodeRequest(_message.Message):
    __slots__ = ("email", "verify_code")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    VERIFY_CODE_FIELD_NUMBER: _ClassVar[int]
    email: str
    verify_code: int
    def __init__(self, email: _Optional[str] = ..., verify_code: _Optional[int] = ...) -> None: ...

class ResendVerifyCodeResponse(_message.Message):
    __slots__ = ("id", "email", "title", "refresh_token", "access_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    title: str
    refresh_token: str
    access_token: str
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., title: _Optional[str] = ..., refresh_token: _Optional[str] = ..., access_token: _Optional[str] = ...) -> None: ...

class VerifyAccountRequest(_message.Message):
    __slots__ = ("email", "verify_code")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    VERIFY_CODE_FIELD_NUMBER: _ClassVar[int]
    email: str
    verify_code: int
    def __init__(self, email: _Optional[str] = ..., verify_code: _Optional[int] = ...) -> None: ...

class VerifyAccountResponse(_message.Message):
    __slots__ = ("id", "email", "title", "refresh_token", "access_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    title: str
    refresh_token: str
    access_token: str
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., title: _Optional[str] = ..., refresh_token: _Optional[str] = ..., access_token: _Optional[str] = ...) -> None: ...

class NewTokensRequest(_message.Message):
    __slots__ = ("refresh_token",)
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ...) -> None: ...

class NewTokensResponse(_message.Message):
    __slots__ = ("refresh_token", "access_token")
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    access_token: str
    def __init__(self, refresh_token: _Optional[str] = ..., access_token: _Optional[str] = ...) -> None: ...

class RegisterRequest(_message.Message):
    __slots__ = ("email", "password", "name")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    name: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: str
    def __init__(self, ok: _Optional[str] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("id", "email", "title", "refresh_token", "access_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    title: str
    refresh_token: str
    access_token: str
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., title: _Optional[str] = ..., refresh_token: _Optional[str] = ..., access_token: _Optional[str] = ...) -> None: ...
