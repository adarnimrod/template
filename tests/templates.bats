#!/usr/bin/env bats

export name='John'

@test "Basic test" {
    run sh -c "echo 'Hello {{ name }}.' | template"
    [ "$output" = "Hello John." ]
}

@test "Test arguments and reading and to/ from a file" {
    template --output "$BATS_TMPDIR/output" "$BATS_TEST_DIRNAME/input"
    run cat "$BATS_TMPDIR/output"
    [ "$output" = "John" ]
}

@test "Render file in-place" {
    cp "$BATS_TEST_DIRNAME/input" "$BATS_TMPDIR/inplace"
    template --output "$BATS_TMPDIR/inplace" "$BATS_TMPDIR/inplace"
    run cat "$BATS_TMPDIR/inplace"
    [ "$output" = "John" ]
}
