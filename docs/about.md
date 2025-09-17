# HashWizard

## About
HashWizard — прямой и функциональный hash brute-forcer.  
Он выполняет словарные, масочные, rule- и чисто брутфорс-атаки для поиска исходной строки по хешу. Инструмент технический и прагматичный: делает ровно то, что должен — перебирает варианты и возвращает совпадения.

''
  ## Quick facts
- Version: 0.1  
- Project start: 2025-09-09  
- Idea conceived: February 2025  
- Languages: Batch, Python, C  
- Initial platform: Windows (cross-platform planned)
- '''

## Capabilities
- Dictionary attacks with transformation rules  
- Mask/charset brute-force (configurable masks)  
- Combinator attacks (word1+word2, permutations)  
- Rule-based modifications (leet, append/prepend, case)  
- Read-only rainbow table lookups  
- Modular plugin points for new algorithms/transforms

## Usage
HashWizard expects hashes and candidate lists. Provide target hashes and wordlists; engine will attempt recovery using the configured strategies and rules. Output is logged to results/ and logs/.

## Distribution & Monetization
Hobbyist project. Donations accepted. Source code and license included in repo.

## Branding & Provenance
Independent project inspired by community tools. No affiliation with or claim to other projects' trademarks.

## Legal note
This is a brute-forcing tool. Use only on data and systems you are explicitly authorized to test.
