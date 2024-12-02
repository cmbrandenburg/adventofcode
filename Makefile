.PHONY: test
test:
	python3 -m pytest -q day*.py

inputs = $(addprefix input/, $(patsubst day%.py, %, $(wildcard day*.py)))
$(inputs):
	@[ -n "$(SESSION)" ] || { \
		echo "SESSION variable is not set; must be of form 'session=...'; use browser to collect Cookie from website" >&2; \
		exit 1; }
	@mkdir -p $(@D)
	curl -q https://adventofcode.com/2024/day/$(@F)/input -b $(SESSION) >$@

.PHONY: input
input: $(inputs)

