# QASA: Advanced Question Answering on Scientific Articles

## Overview
This repository provides QASA dataset of the following paper:
**[QASA: Advanced Question Answering on Scientific Articles](https://openreview.net/pdf?id=5ud0h8OXwD)**
* Authors: {Yoonjoo Lee*, Kyungjae Lee*}, Sunghyun Park, Dasol Hwang, Jaehyeon Kim, Hong-in Lee, Moontae Lee (* Equal Contribution)
* _ICML 2023_ 

---
## Dataset

- The original benchmark (1798 examples mentioned in our paper) can be found at `data/v0/testset_1798_v0.json`
- After paper submission, we found noisy cases that are unanswerable in a given paper.
- Therefore, we classified the unanswerable cases, and release a separated version (v1): answerable (`data/testset_answerable_1554_v1.json`) & unanswerable (`data/testset_unanswerable_244_v1.json`).
- Released a minor updated version (v1.1) of QASA containing the URL to access the full text. (`data/testset_answerable_1554_v1.1.json`, `data/testset_answerable_1554_v1.1.json`)
---

## License
```
QASA

MIT License

Copyright (c) 2023 LG AI Research

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
## How to cite

```
@inproceedings{lee2023qasa,
  title={QASA: Advanced Question Answering on Scientific Articles},
  author={Lee, Yoonjoo and Lee, Kyungjae and Park, Sunghyun and Hwang, Dasol and Kim, Jaehyeon and Lee, Hong-in and Lee, Moontae},
  booktitle={Proceedings of the 40th International Conference on Machine Learning},
  year={2023}
}
```

## Contact
If you have any questions, please send an email to: Moontae Lee (moontae.lee@lgresearch.ai)
