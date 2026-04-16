# OMNIABASE Minimal Structural Reliability Demo v0

## Goal

Show that surface correctness and structural reliability are not the same thing.

## Input

A shop sells 3 boxes.
Each box contains 4 items.
How many items are there in total?

## Outputs

### Output A
There are 12 items in total.

### Output B
There are 12 items in total because 3 + 4 + 5 = 12.

### Output C
There are 11 items in total.

## Expected structural reading

- Output A:
  - final answer: correct
  - internal structure: coherent
  - reliability: high

- Output B:
  - final answer: correct
  - internal structure: incoherent
  - reliability: low
  - note: surface success, structural failure

- Output C:
  - final answer: incorrect
  - internal structure: unstable
  - reliability: low

## Core claim

A representation can look acceptable at the surface level while remaining structurally unreliable.

OMNIABASE is useful if it can separate:

- surface validity
- structural validity

This separation is the first minimal proof of value.