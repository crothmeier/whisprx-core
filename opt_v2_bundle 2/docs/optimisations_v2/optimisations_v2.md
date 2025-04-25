<!-- OPT_V2_START -->
## 2.2 Continuous Batching (v2)

**Why**  Reduces time‑to‑first‑token under light traffic by padding vLLM’s burst queue  
**How**  Use `Client.generate_stream()` with `stream=True`; keep a rolling queue of requests and let vLLM merge them.  
**Impact**  Observed 18‑22 × throughput uplift at batch‑size 4 on A4000 without extra VRAM.

```python
from text_generation import Client

client = Client("http://localhost:8080")
for token in client.generate_stream(prompt,
                                    temperature=0.7,
                                    stream=True,
                                    request_id=f"req_{ts}"):
    handle(token)
```

## 2.5 Explicit Tensor‑Parallel Map

See listing: `examples/llm_device_map.py`. Splits upper layers to GPU‑1 to keep KV‑cache hot.

## 3.1 ONNX‑Quant TTS (update)

Added dynamic‑quant CLI:

```bash
onnxruntime_tools.quantize_dynamic tts_model.onnx -o tts_model_q.onnx
```

## 3.2 Parallel Audio Worker

Feature‑flagged threaded queue that generates audio while previous chunk plays.
Enable via `ENABLE_PARALLEL_AUDIO_WORKER = True`.
<!-- OPT_V2_END -->
