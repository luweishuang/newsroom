newsroom-scrape --urls data/urls.txt --archive data/test.archive

newsroom-extract --archive data/test.archive --dataset data/test.dataset

newsroom-run --system textrank --dataset data/test.dataset --summaries data/test.summaries
