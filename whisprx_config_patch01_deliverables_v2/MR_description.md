# Merge Request: Config-Patch-01 – Performance Preset Integration

**Highlights**

* Adds `performance_presets.yaml` with *ultra_low_latency* and *balanced* profiles.
* New `load_performance_profile()` helper and wiring into `audio_buffer` & `cuda_utils`.
* Optional Torch‑TensorRT toggle with graceful fallback.
* Sentence‑level streaming in `tts_streamer` plus defensive mode assertion.
* Comprehensive unit test `test_tts_split.py` (basic, complex, empty, no‑punctuation).
* Docs refreshed with preset table and file link.

All tests (`pytest -q`) and lint (`flake8`) pass. CI green.
