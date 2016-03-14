#!/bin/sh -e

test "$(echo '{{ name }}' | name='Nimrod' template)" = "Nimrod"
