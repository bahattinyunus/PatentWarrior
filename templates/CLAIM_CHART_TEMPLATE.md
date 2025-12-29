# ⚖️ Patent Claim Chart Template

## Case Information
- **Target Patent**: [Patent Number, e.g., US12345678B2]
- **Target Product/Code**: [Product Name or Source Code File]
- **Date**: [YYYY-MM-DD]
- **Analyst**: [Your Name/Alias]

## Instructions
1. Break down the patent claim into individual "elements" (clauses).
2. For each element, find the corresponding feature in the prior art or the target product.
3. Be precise. If an element is "a red ball," and the product has "a blue cube," it is a mismatch.

## Claim 1 Analysis

| Claim Element (The "Attack") | Evidence / Prior Art (The "Shield") | Analysis / Notes |
| :--- | :--- | :--- |
| **1(a)** A method for processing data comprising: | **Source:** `utils.py`, line 45 | Preamble. Matches general function of module. |
| **1(b)** receiving a first signal from a sensor; | **Source:** `sensor_input.c`, function `read_signal()` | The code reads `signal_a` from the GPIO pin, which corresponds to the "first signal". |
| **1(c)** transforming said signal using a Fourier transform; | **Source:** [Prior Art: IEEE Paper 2015 - Smith et al.] | **INVALIDITY POINT**: This step was disclosed in Smith 2015, page 3. The patent is potentially invalid here due to obviousness. |
| **1(d)** outputting a frequency spectrum. | **Source:** N/A | **Does not match**. Our product outputs a time-domain graph, not a frequency spectrum. |

## Conclusion
[ ] **Infringement Likely**: All elements match.
[ ] **Non-Infringement**: At least one element is missing (e.g., 1(d)).
[ ] **Invalidity Found**: Prior art covers all elements.

## Strategy
- If **Non-Infringement**: Prepare technical opinion letter.
- If **Invalidity**: Prepare Third-Party Preissuance Submission or Post-Grant Review request.
