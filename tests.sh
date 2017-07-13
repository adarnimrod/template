#!/bin/sh
set -eu

infile="$(mktemp)"
outfile="$(mktemp)"
export infile outfile

echo Basic test.
export name='John'
test "$(echo 'Hello {{ name if name is defined else "world" }}.' | template)" = "Hello John."

echo Testing arguments and reading/ writing to file.
echo '{{ name }}' > "$infile"
export name='John'
template --output "$outfile" "$infile"
test "$(cat "$outfile")" = "$name"

rm "$infile" "$outfile"
