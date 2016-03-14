#!/bin/sh -e

export infile="$(mktemp)"
export outfile="$(mktemp)"

echo Basic test.
export name='John'
test "$(echo 'Hello {{ name if name is defined else 'world' }}.' | template)" = "Hello John."

echo Testing arguments and reading/ writing to file.
echo '{{ USER }}' > "$infile"
template --output "$outfile" "$infile"
test "$(cat $outfile)" = "$USER"

echo Testing JSON parsing.
export json='{"a": 1, "b": 2}'
echo '{{ (json|from_json)["a"] }}' > "$infile"
test "$(template $infile)" = "1"

echo Testing JSON output.
echo '{{ [1, 1+2, 3] | to_json }}' > "$infile"
test "$(template $infile)" = '[1, 3, 3]'

echo Testing YAML parsing.
export yaml='a: 1
b: 2'
echo '{{ (yaml|from_yaml)["a"] }}' > "$infile"
test "$(template $infile)" = "1"

echo Testing YAML output.
echo '{{ [1, 1+2, 3] | to_yaml }}' > "$infile"
test "$(template $infile)" = '[1, 3, 3]'

echo Testing pprint.
echo '{{ [1, ] + [2, ] }}' > "$infile"
test "$(template $infile)" = "[1, 2]"

echo Testing combining dictionaries.

rm "$infile" "$outfile"
