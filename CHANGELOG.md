## WIP

### Fixed
- Fix `LabUnc.__eq__` raising `AttributeError` when compared with an object without `n` and `s` attributes (e.g., `LabUnc(1, 0) == 5`). Unsupported comparisons now return `NotImplemented` instead of raising an error.

### Changed
- Remove the unnecessary Python version check for importing `Self`, since the minimum supported Python version is 3.11.

## Version 0.1: start of assignment

- First code.
