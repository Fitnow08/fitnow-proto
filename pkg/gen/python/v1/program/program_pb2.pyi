from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DifficultyLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIFFICULTY_LEVEL_UNSPECIFIED: _ClassVar[DifficultyLevel]
    DIFFICULTY_LEVEL_EASY: _ClassVar[DifficultyLevel]
    DIFFICULTY_LEVEL_MEDIUM: _ClassVar[DifficultyLevel]
    DIFFICULTY_LEVEL_HARD: _ClassVar[DifficultyLevel]
DIFFICULTY_LEVEL_UNSPECIFIED: DifficultyLevel
DIFFICULTY_LEVEL_EASY: DifficultyLevel
DIFFICULTY_LEVEL_MEDIUM: DifficultyLevel
DIFFICULTY_LEVEL_HARD: DifficultyLevel

class DeleteProgramCategoryResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteProgramCategoryRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class UpdateProgramCategoryRequest(_message.Message):
    __slots__ = ("id", "title")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class UpdateProgramCategoryResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateProgramCategoryRequest(_message.Message):
    __slots__ = ("title",)
    TITLE_FIELD_NUMBER: _ClassVar[int]
    title: str
    def __init__(self, title: _Optional[str] = ...) -> None: ...

class CreateProgramCategoryResponse(_message.Message):
    __slots__ = ("train",)
    TRAIN_FIELD_NUMBER: _ClassVar[int]
    train: ProgramCategory
    def __init__(self, train: _Optional[_Union[ProgramCategory, _Mapping]] = ...) -> None: ...

class GetAllProgramCategoryRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAllProgramCategoryResponse(_message.Message):
    __slots__ = ("train",)
    TRAIN_FIELD_NUMBER: _ClassVar[int]
    train: _containers.RepeatedCompositeFieldContainer[ProgramCategory]
    def __init__(self, train: _Optional[_Iterable[_Union[ProgramCategory, _Mapping]]] = ...) -> None: ...

class ProgramCategory(_message.Message):
    __slots__ = ("id", "name", "updated_at", "created_at", "version")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    updated_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    version: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class UploadAllProgramTrainsRequest(_message.Message):
    __slots__ = ("program_id", "trains")
    PROGRAM_ID_FIELD_NUMBER: _ClassVar[int]
    TRAINS_FIELD_NUMBER: _ClassVar[int]
    program_id: str
    trains: _containers.RepeatedCompositeFieldContainer[ProgramTrainInput]
    def __init__(self, program_id: _Optional[str] = ..., trains: _Optional[_Iterable[_Union[ProgramTrainInput, _Mapping]]] = ...) -> None: ...

class UploadAllProgramTrainsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProgramTrainInput(_message.Message):
    __slots__ = ("train_id", "week_number", "day_of_week", "position")
    TRAIN_ID_FIELD_NUMBER: _ClassVar[int]
    WEEK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    train_id: str
    week_number: int
    day_of_week: int
    position: int
    def __init__(self, train_id: _Optional[str] = ..., week_number: _Optional[int] = ..., day_of_week: _Optional[int] = ..., position: _Optional[int] = ...) -> None: ...

class AddProgramTrainsRequest(_message.Message):
    __slots__ = ("program_id", "trains")
    PROGRAM_ID_FIELD_NUMBER: _ClassVar[int]
    TRAINS_FIELD_NUMBER: _ClassVar[int]
    program_id: str
    trains: _containers.RepeatedCompositeFieldContainer[ProgramTrainInput]
    def __init__(self, program_id: _Optional[str] = ..., trains: _Optional[_Iterable[_Union[ProgramTrainInput, _Mapping]]] = ...) -> None: ...

class GetProgramsAndTrainsRequest(_message.Message):
    __slots__ = ("program_id",)
    PROGRAM_ID_FIELD_NUMBER: _ClassVar[int]
    program_id: str
    def __init__(self, program_id: _Optional[str] = ...) -> None: ...

class GetProgramsAndTrainsResponse(_message.Message):
    __slots__ = ("program", "trains")
    PROGRAM_FIELD_NUMBER: _ClassVar[int]
    TRAINS_FIELD_NUMBER: _ClassVar[int]
    program: Program
    trains: _containers.RepeatedCompositeFieldContainer[ProgramTrain]
    def __init__(self, program: _Optional[_Union[Program, _Mapping]] = ..., trains: _Optional[_Iterable[_Union[ProgramTrain, _Mapping]]] = ...) -> None: ...

class Program(_message.Message):
    __slots__ = ("id", "title", "weeks", "difficulty", "is_public", "category_id", "image_url", "created_at", "updated_at", "version", "desc", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    WEEKS_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    weeks: int
    difficulty: str
    is_public: bool
    category_id: str
    image_url: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    version: int
    desc: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., weeks: _Optional[int] = ..., difficulty: _Optional[str] = ..., is_public: bool = ..., category_id: _Optional[str] = ..., image_url: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ..., desc: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class Train(_message.Message):
    __slots__ = ("id", "title", "type", "duration", "is_public", "difficulty", "calories", "category_id", "image_url", "created_by", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    CALORIES_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    type: str
    duration: int
    is_public: bool
    difficulty: str
    calories: int
    category_id: str
    image_url: str
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., type: _Optional[str] = ..., duration: _Optional[int] = ..., is_public: bool = ..., difficulty: _Optional[str] = ..., calories: _Optional[int] = ..., category_id: _Optional[str] = ..., image_url: _Optional[str] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ProgramTrain(_message.Message):
    __slots__ = ("train", "week_number", "day_of_week", "position")
    TRAIN_FIELD_NUMBER: _ClassVar[int]
    WEEK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    train: Train
    week_number: int
    day_of_week: int
    position: int
    def __init__(self, train: _Optional[_Union[Train, _Mapping]] = ..., week_number: _Optional[int] = ..., day_of_week: _Optional[int] = ..., position: _Optional[int] = ...) -> None: ...

class AddProgramImageRequest(_message.Message):
    __slots__ = ("program_id", "extension", "content_type", "image")
    PROGRAM_ID_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    program_id: str
    extension: str
    content_type: str
    image: bytes
    def __init__(self, program_id: _Optional[str] = ..., extension: _Optional[str] = ..., content_type: _Optional[str] = ..., image: _Optional[bytes] = ...) -> None: ...

class AddProgramImageResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateProgramRequest(_message.Message):
    __slots__ = ("title", "description", "weeks", "difficulty", "category_id", "user_id")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WEEKS_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    weeks: int
    difficulty: DifficultyLevel
    category_id: str
    user_id: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., weeks: _Optional[int] = ..., difficulty: _Optional[_Union[DifficultyLevel, str]] = ..., category_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class CreateProgramResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAllProgramsRequest(_message.Message):
    __slots__ = ("category_id", "search")
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    category_id: str
    search: str
    def __init__(self, category_id: _Optional[str] = ..., search: _Optional[str] = ...) -> None: ...

class GetAllProgramsResponse(_message.Message):
    __slots__ = ("programs",)
    PROGRAMS_FIELD_NUMBER: _ClassVar[int]
    programs: _containers.RepeatedCompositeFieldContainer[ProgramAndTrainsCount]
    def __init__(self, programs: _Optional[_Iterable[_Union[ProgramAndTrainsCount, _Mapping]]] = ...) -> None: ...

class ProgramAndTrainsCount(_message.Message):
    __slots__ = ("id", "title", "desc", "weeks", "difficulty", "is_public", "category_id", "image_path", "image_url", "created_by", "created_at", "updated_at", "version", "trains_count")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    WEEKS_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_PATH_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TRAINS_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    desc: str
    weeks: int
    difficulty: str
    is_public: bool
    category_id: str
    image_path: str
    image_url: str
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    version: int
    trains_count: int
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., desc: _Optional[str] = ..., weeks: _Optional[int] = ..., difficulty: _Optional[str] = ..., is_public: bool = ..., category_id: _Optional[str] = ..., image_path: _Optional[str] = ..., image_url: _Optional[str] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ..., trains_count: _Optional[int] = ...) -> None: ...
