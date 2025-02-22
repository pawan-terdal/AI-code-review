# AI-code-review

## What it does? 
Any PR opened to this repo will be automatically reviewed by AI and will post review comments on the PR 

## How to use
You can reference this workflow in your workflow by adding below line to the 'uses' section 

    pawan-terdal/ai-code-review-bot/.github/workflows/code-review-bot.yml@main

## Example

      name: Use AI Code Review Bot
      
      on:
        pull_request:
          types: [opened, synchronize, reopened]
      
      jobs:
        run-code-review:
          ### uses: your-username/ai-code-review-bot/.github/workflows/code-review-bot.yml@main
          with:
            repo: ${{ github.repository }}
            pr_number: ${{ github.event.pull_request.number }}
          secrets:
            GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
