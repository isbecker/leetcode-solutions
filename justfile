# Get the directory of the current justfile
default: all

run NUM:
    @echo "Running {{NUM}}..."
    rye run python src/{{NUM}}/main.py

add DEP:
	rye add {{DEP}}

install DEP:
    rye install {{DEP}}

sync:
	rye sync

shell:
    rye shell

lint:
    rye lint

fmt:
    rye format

fix: fmt lint

test:
    rye test

all: sync lint fmt
