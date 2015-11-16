#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some debugging practice."""


class CustomError(Exception):
    """CustomError extends the Exception class."""

    def __init__(self, cause):
        """Constructor docstring."""
        self.cause = cause
