# Copyright (c) 2025 - 2026, HaiyangLi <quantocean.li at gmail dot com>
# SPDX-License-Identifier: Apache-2.0

"""Core primitives with lazy loading for fast import."""

from __future__ import annotations

from typing import TYPE_CHECKING

# Lazy import mapping
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # broadcaster
    "Broadcaster": ("kron.core.broadcaster", "Broadcaster"),
    # element
    "Element": ("kron.core.element", "Element"),
    # event
    "Event": ("kron.core.event", "Event"),
    "EventStatus": ("kron.core.event", "EventStatus"),
    "Execution": ("kron.core.event", "Execution"),
    # eventbus
    "EventBus": ("kron.core.eventbus", "EventBus"),
    "Handler": ("kron.core.eventbus", "Handler"),
    # flow
    "Flow": ("kron.core.flow", "Flow"),
    # graph
    "Edge": ("kron.core.graph", "Edge"),
    "EdgeCondition": ("kron.core.graph", "EdgeCondition"),
    "Graph": ("kron.core.graph", "Graph"),
    # node
    "DEFAULT_NODE_CONFIG": ("kron.core.node", "DEFAULT_NODE_CONFIG"),
    "NODE_REGISTRY": ("kron.core.node", "NODE_REGISTRY"),
    "PERSISTABLE_NODE_REGISTRY": ("kron.core.node", "PERSISTABLE_NODE_REGISTRY"),
    "Node": ("kron.core.node", "Node"),
    "NodeConfig": ("kron.core.node", "NodeConfig"),
    "create_node": ("kron.core.node", "create_node"),
    "generate_ddl": ("kron.core.node", "generate_ddl"),
    # phrase
    "PHRASE_REGISTRY": ("kron.core.phrase", "PHRASE_REGISTRY"),
    "Phrase": ("kron.core.phrase", "Phrase"),
    "PhraseConfig": ("kron.core.phrase", "PhraseConfig"),
    "PhraseError": ("kron.core.phrase", "PhraseError"),
    "RequirementNotMet": ("kron.core.phrase", "RequirementNotMet"),
    "create_phrase": ("kron.core.phrase", "create_phrase"),
    "get_phrase": ("kron.core.phrase", "get_phrase"),
    "list_phrases": ("kron.core.phrase", "list_phrases"),
    # pile
    "Pile": ("kron.core.pile", "Pile"),
    # processor
    "Executor": ("kron.core.processor", "Executor"),
    "Processor": ("kron.core.processor", "Processor"),
    # progression
    "Progression": ("kron.core.progression", "Progression"),
}

_LOADED: dict[str, object] = {}


def __getattr__(name: str) -> object:
    """Lazy import attributes on first access."""
    if name in _LOADED:
        return _LOADED[name]

    if name in _LAZY_IMPORTS:
        from importlib import import_module

        module_name, attr_name = _LAZY_IMPORTS[name]
        module = import_module(module_name)
        value = getattr(module, attr_name)
        _LOADED[name] = value
        return value

    raise AttributeError(f"module 'kron.core' has no attribute {name!r}")


def __dir__() -> list[str]:
    """Return all available attributes for autocomplete."""
    return list(__all__)


# TYPE_CHECKING block for static analysis
if TYPE_CHECKING:
    from .broadcaster import Broadcaster
    from .element import Element
    from .event import Event, EventStatus, Execution
    from .eventbus import EventBus, Handler
    from .flow import Flow
    from .graph import Edge, EdgeCondition, Graph
    from .node import (
        DEFAULT_NODE_CONFIG,
        NODE_REGISTRY,
        PERSISTABLE_NODE_REGISTRY,
        Node,
        NodeConfig,
        create_node,
        generate_ddl,
    )
    from .phrase import (
        PHRASE_REGISTRY,
        Phrase,
        PhraseConfig,
        PhraseError,
        RequirementNotMet,
        create_phrase,
        get_phrase,
        list_phrases,
    )
    from .pile import Pile
    from .processor import Executor, Processor
    from .progression import Progression

__all__ = [
    # constants
    "DEFAULT_NODE_CONFIG",
    "NODE_REGISTRY",
    "PERSISTABLE_NODE_REGISTRY",
    "PHRASE_REGISTRY",
    # classes
    "Broadcaster",
    "Edge",
    "EdgeCondition",
    "Element",
    "Event",
    "EventBus",
    "EventStatus",
    "Execution",
    "Executor",
    "Flow",
    "Graph",
    "Handler",
    "Node",
    "NodeConfig",
    "Phrase",
    "PhraseConfig",
    "PhraseError",
    "Pile",
    "Processor",
    "Progression",
    "RequirementNotMet",
    # functions
    "create_node",
    "create_phrase",
    "generate_ddl",
    "get_phrase",
    "list_phrases",
]
