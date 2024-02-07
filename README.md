# Gronk Overview

## 🚨 Problem

The next generation of LLM application infrastructure will be software that makes LLM apps generate higher quality content. However, the state of the art for implementing quality of content content requires deep, specific knowledge of the following techniques:
1. A way to verify the quality of dynamically generated content at runtime
2. A way to improve the performance and sourcing of RAG applications as compared to what you get out of the box
3. A way to automatically optimize prompts at runtime given *i* max cycles or *t* max runtime
4. Create and string together thought chains (CoT) and thought trees (ToT).
5. Implement an [active CoT]([url](https://arxiv.org/abs/2302.12246)) toolkit 
6. Use specific CoT/ToT technique that improve content beyond what you get out of the box
7. Build and mantain a debugging app for the LLM application to iterate and improve content

## 💡 Solution

To solve these problems, developers need access to a robust toolkit that's **easy to use and understand** and **performs significantly better than vanilla implementations**. This toolkit should allow developers to solve these problems in just a few lines of code, in a way that's easy for them to explain to their team.

## 🤯 The Next Generation of LLM Application Infrastructure

Currently, here's the state of play for LLM application infrastructure

| Software | |
| ------------ | ----------- |
| Application | Above the fold |
| **Quality of Content Infrastructure** | this repo |
| **Quality of Life Infrastructure** | RAG, prompt chains, prompt lifecycle management, agents, etc. |
| **Core Functionalities** | vector databases, synthetic data, similarity search, LLM libraries, etc. |
| LLM(s) | Below the fold |
