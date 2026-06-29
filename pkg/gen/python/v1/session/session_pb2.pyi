from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorkoutSession(_message.Message):
    __slots__ = ("id", "user_id", "train_id", "program_train_id", "duration", "calories", "completed_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_TRAIN_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    CALORIES_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    train_id: str
    program_train_id: str
    duration: int
    calories: int
    completed_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., train_id: _Optional[str] = ..., program_train_id: _Optional[str] = ..., duration: _Optional[int] = ..., calories: _Optional[int] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateWorkoutSessionRequest(_message.Message):
    __slots__ = ("user_id", "train_id", "program_train_id", "duration", "calories")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_TRAIN_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    CALORIES_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    train_id: str
    program_train_id: str
    duration: int
    calories: int
    def __init__(self, user_id: _Optional[str] = ..., train_id: _Optional[str] = ..., program_train_id: _Optional[str] = ..., duration: _Optional[int] = ..., calories: _Optional[int] = ...) -> None: ...

class CreateWorkoutSessionResponse(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: WorkoutSession
    def __init__(self, session: _Optional[_Union[WorkoutSession, _Mapping]] = ...) -> None: ...

class GetWorkoutSessionsRequest(_message.Message):
    __slots__ = ("user_id", "to", "limit", "cursor")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    to: _timestamp_pb2.Timestamp
    limit: int
    cursor: str
    def __init__(self, user_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ..., **kwargs) -> None: ...

class GetWorkoutSessionsResponse(_message.Message):
    __slots__ = ("sessions", "next_cursor", "has_more")
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[WorkoutSession]
    next_cursor: str
    has_more: bool
    def __init__(self, sessions: _Optional[_Iterable[_Union[WorkoutSession, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., has_more: bool = ...) -> None: ...

class SessionNote(_message.Message):
    __slots__ = ("id", "user_id", "session_id", "note", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    session_id: str
    note: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., session_id: _Optional[str] = ..., note: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpsertSessionNoteRequest(_message.Message):
    __slots__ = ("user_id", "session_id", "note")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_id: str
    note: str
    def __init__(self, user_id: _Optional[str] = ..., session_id: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class UpsertSessionNoteResponse(_message.Message):
    __slots__ = ("note",)
    NOTE_FIELD_NUMBER: _ClassVar[int]
    note: SessionNote
    def __init__(self, note: _Optional[_Union[SessionNote, _Mapping]] = ...) -> None: ...

class GetSessionNotesRequest(_message.Message):
    __slots__ = ("session_id", "user_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_id: str
    def __init__(self, session_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class GetSessionNotesResponse(_message.Message):
    __slots__ = ("notes",)
    NOTES_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedCompositeFieldContainer[SessionNote]
    def __init__(self, notes: _Optional[_Iterable[_Union[SessionNote, _Mapping]]] = ...) -> None: ...

class DeleteSessionNoteRequest(_message.Message):
    __slots__ = ("id", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class DeleteSessionNoteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SessionExerciseNote(_message.Message):
    __slots__ = ("id", "user_id", "session_id", "exercise_id", "note", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    session_id: str
    exercise_id: str
    note: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., session_id: _Optional[str] = ..., exercise_id: _Optional[str] = ..., note: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpsertSessionExerciseNoteRequest(_message.Message):
    __slots__ = ("user_id", "session_id", "exercise_id", "note")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_id: str
    exercise_id: str
    note: str
    def __init__(self, user_id: _Optional[str] = ..., session_id: _Optional[str] = ..., exercise_id: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class UpsertSessionExerciseNoteResponse(_message.Message):
    __slots__ = ("note",)
    NOTE_FIELD_NUMBER: _ClassVar[int]
    note: SessionExerciseNote
    def __init__(self, note: _Optional[_Union[SessionExerciseNote, _Mapping]] = ...) -> None: ...

class GetSessionExerciseNotesRequest(_message.Message):
    __slots__ = ("session_id", "user_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_id: str
    def __init__(self, session_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class GetSessionExerciseNotesResponse(_message.Message):
    __slots__ = ("notes",)
    NOTES_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedCompositeFieldContainer[SessionExerciseNote]
    def __init__(self, notes: _Optional[_Iterable[_Union[SessionExerciseNote, _Mapping]]] = ...) -> None: ...

class DeleteSessionExerciseNoteRequest(_message.Message):
    __slots__ = ("id", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class DeleteSessionExerciseNoteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
