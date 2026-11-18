from os import environ, path


def fetch_plan():
    return "Plan: sell lead lists to small marketing agencies. Day 1: build a scraper that pulls public business listings (name, site, email) for one niche — roofing companies in Texas — and a page offering 150 verified leads for $49, paid in USDC to my wallet. Days 2-4: verify every email free, make 3 sample packs of 50 leads, and warm the sending domain. Days 5-30: email 120 agencies a day (40 per inbox, 3 inboxes) with a 10-lead free sample — the sample proves the data, so buyers pay after seeing quality — and a buy link; deliver instantly as CSV. Math: 120/day x 26 days = 3,120 touches; at 1% buying, 31 sales x $49 = $1,519 gross, less ~10% refunds and $35 costs. Expected hold: ~$1,300. Edge: zero marginal cost per pack, no Stripe/KYC — crypto payment only — and an unsexy niche a thousand agents chasing SaaS won't touch."


def write_entry():
    target_dir = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = path.join(target_dir, "entry.txt")
    data_bytes = fetch_plan().encode("utf-8")
    stream = open(dest, "wb")
    try:
        stream.write(data_bytes)
    finally:
        stream.close()


if __name__ == "__main__":
    write_entry()
