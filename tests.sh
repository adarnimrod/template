#!/bin/sh -e

export name='John'
test "$(echo 'Hello {{ name if name is defined else 'world' }}.' | template)" = "Hello John."
export infile="$(mktemp)"
export outfile="$(mktemp)"
echo '{{ USER }}' > "$infile"
template --output "$outfile" "$infile"
test "$(cat $outfile)" = "$USER"
rm "$infile" "$outfile"
