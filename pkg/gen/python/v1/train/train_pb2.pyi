from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrainType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRAIN_TYPE_UNSPECIFIED: _ClassVar[TrainType]
    TRAIN_TYPE_STRENGTH: _ClassVar[TrainType]
    TRAIN_TYPE_CARDIO: _ClassVar[TrainType]
    TRAIN_TYPE_STRETCHING: _ClassVar[TrainType]

class Difficulty(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIFFICULTY_UNSPECIFIED: _ClassVar[Difficulty]
    DIFFICULTY_EASY: _ClassVar[Difficulty]
    DIFFICULTY_MEDIUM: _ClassVar[Difficulty]
    DIFFICULTY_HARD: _ClassVar[Difficulty]
TRAIN_TYPE_UNSPECIFIED: TrainType
TRAIN_TYPE_STRENGTH: TrainType
TRAIN_TYPE_CARDIO: TrainType
TRAIN_TYPE_STRETCHING: TrainType
DIFFICULTY_UNSPECIFIED: Difficulty
DIFFICULTY_EASY: Difficulty
DIFFICULTY_MEDIUM: Difficulty
DIFFICULTY_HARD: Difficulty

class AddTrainExercisesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddTrainExercisesRequest(_message.Message):
    __slots__ = ("train_id", "exercises")
    TRAIN_ID_FIELD_NUMBER: _ClassVar[int]
    EXERCISES_FIELD_NUMBER: _ClassVar[int]
    train_id: str
    exercises: _containers.RepeatedCompositeFieldContainer[TrainExerciseInput]
    def __init__(self, train_id: _Optional[str] = ..., exercises: _Optional[_Iterable[_Union[TrainExerciseInput, _Mapping]]] = ...) -> None: ...

class GetTrainAndExercisesRequest(_message.Message):
    __slots__ = ("strain_id",)
    STRAIN_ID_FIELD_NUMBER: _ClassVar[int]
    strain_id: str
    def __init__(self, strain_id: _Optional[str] = ...) -> None: ...

class GetTrainAndExercisesResponse(_message.Message):
    __slots__ = ("train", "exercises")
    TRAIN_FIELD_NUMBER: _ClassVar[int]
    EXERCISES_FIELD_NUMBER: _ClassVar[int]
    train: Train
    exercises: _containers.RepeatedCompositeFieldContainer[TrainExercise]
    def __init__(self, train: _Optional[_Union[Train, _Mapping]] = ..., exercises: _Optional[_Iterable[_Union[TrainExercise, _Mapping]]] = ...) -> None: ...

class GetAllAdminTrainsResponse(_message.Message):
    __slots__ = ("trains", "total_count")
    TRAINS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    trains: _containers.RepeatedCompositeFieldContainer[Train]
    total_count: int
    def __init__(self, trains: _Optional[_Iterable[_Union[Train, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class GetAllAdminTrainsRequest(_message.Message):
    __slots__ = ("page", "limit", "category_id", "text")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    page: int
    limit: int
    category_id: str
    text: str
    def __init__(self, page: _Optional[int] = ..., limit: _Optional[int] = ..., category_id: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class AddTrainImageResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddTrainImageRequest(_message.Message):
    __slots__ = ("train_id", "extension", "content_type", "image")
    TRAIN_ID_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    train_id: str
    extension: str
    content_type: str
    image: bytes
    def __init__(self, train_id: _Optional[str] = ..., extension: _Optional[str] = ..., content_type: _Optional[str] = ..., image: _Optional[bytes] = ...) -> None: ...

class DeleteTrainResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteTrainRequest(_message.Message):
    __slots__ = ("id", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UpdateTrainResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateTrainRequest(_message.Message):
    __slots__ = ("train_id", "title", "type", "duration", "is_public", "difficulty", "calories", "user_id")
    TRAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    CALORIES_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    train_id: str
    title: str
    type: TrainType
    duration: int
    is_public: bool
    difficulty: Difficulty
    calories: int
    user_id: str
    def __init__(self, train_id: _Optional[str] = ..., title: _Optional[str] = ..., type: _Optional[_Union[TrainType, str]] = ..., duration: _Optional[int] = ..., is_public: bool = ..., difficulty: _Optional[_Union[Difficulty, str]] = ..., calories: _Optional[int] = ..., user_id: _Optional[str] = ...) -> None: ...

class CreateTrainResponse(_message.Message):
    __slots__ = ("train",)
    TRAIN_FIELD_NUMBER: _ClassVar[int]
    train: Train
    def __init__(self, train: _Optional[_Union[Train, _Mapping]] = ...) -> None: ...

class CreateTrainRequest(_message.Message):
    __slots__ = ("title", "type", "duration", "is_public", "difficulty", "calories", "category_id", "user_id")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    CALORIES_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    type: TrainType
    duration: int
    is_public: bool
    difficulty: Difficulty
    calories: int
    category_id: str
    user_id: str
    def __init__(self, title: _Optional[str] = ..., type: _Optional[_Union[TrainType, str]] = ..., duration: _Optional[int] = ..., is_public: bool = ..., difficulty: _Optional[_Union[Difficulty, str]] = ..., calories: _Optional[int] = ..., category_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class GetAllTrainsRequest(_message.Message):
    __slots__ = ("limit", "cursor", "category_id", "text")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    cursor: str
    category_id: str
    text: str
    def __init__(self, limit: _Optional[int] = ..., cursor: _Optional[str] = ..., category_id: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class GetAllTrainsResponse(_message.Message):
    __slots__ = ("trains", "next_cursor", "has_more")
    TRAINS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    trains: _containers.RepeatedCompositeFieldContainer[Train]
    next_cursor: str
    has_more: bool
    def __init__(self, trains: _Optional[_Iterable[_Union[Train, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., has_more: bool = ...) -> None: ...

class Train(_message.Message):
    __slots__ = ("id", "title", "type", "duration", "is_public", "difficulty", "created_by", "created_at", "category_id", "calories", "image_path", "updated_at", "version")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    CALORIES_FIELD_NUMBER: _ClassVar[int]
    IMAGE_PATH_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    type: str
    duration: int
    is_public: bool
    difficulty: str
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    category_id: str
    calories: int
    image_path: str
    updated_at: _timestamp_pb2.Timestamp
    version: int
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., type: _Optional[str] = ..., duration: _Optional[int] = ..., is_public: bool = ..., difficulty: _Optional[str] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., category_id: _Optional[str] = ..., calories: _Optional[int] = ..., image_path: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class TrainExerciseInput(_message.Message):
    __slots__ = ("exercise_id", "steps", "sets", "position", "weight")
    EXERCISE_ID_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    SETS_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    exercise_id: str
    steps: int
    sets: int
    position: int
    weight: float
    def __init__(self, exercise_id: _Optional[str] = ..., steps: _Optional[int] = ..., sets: _Optional[int] = ..., position: _Optional[int] = ..., weight: _Optional[float] = ...) -> None: ...

class TrainExercise(_message.Message):
    __slots__ = ("id", "title", "description", "video_url", "difficulty", "steps", "sets", "position", "weight")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    SETS_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    description: str
    video_url: str
    difficulty: Difficulty
    steps: int
    sets: int
    position: int
    weight: float
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., video_url: _Optional[str] = ..., difficulty: _Optional[_Union[Difficulty, str]] = ..., steps: _Optional[int] = ..., sets: _Optional[int] = ..., position: _Optional[int] = ..., weight: _Optional[float] = ...) -> None: ...
