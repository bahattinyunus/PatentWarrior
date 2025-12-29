import argparse
import urllib.parse
import sys

def create_google_patents_url(keywords, assignee=None, inventor=None, before=None, after=None):
    base_url = "https://patents.google.com/?"
    params = []
    
    # Basic query construction
    q = " ".join(f'"{k}"' if " " in k else k for k in keywords)
    
    if assignee:
        q += f" assignee:({assignee})"
    if inventor:
        q += f" inventor:({inventor})"
    if before:
        q += f" before:priority:{before}"
    if after:
        q += f" after:priority:{after}"
        
    params.append(f"q={urllib.parse.quote(q)}")
    
    return base_url + "&".join(params)

def create_espacenet_url(keywords):
    # Espacenet uses a different structure, simplified here
    base_url = "https://worldwide.espacenet.com/patent/search?q="
    query_parts = []
    for k in keywords:
        query_parts.append(k)
    
    return base_url + urllib.parse.quote(" AND ".join(query_parts))

def create_uspto_url(keywords):
    # USPTO Patent Public Search is complex to deep link into with queries, 
    # but we can provide a basic query string for manual entry
    q = " AND ".join(f'"{k}"' if " " in k else k for k in keywords)
    return f"USPTO Query String (Copy & Paste): {q}"

def main():
    parser = argparse.ArgumentParser(description="PatentWarrior Query Generator - Create advanced search URLs")
    parser.add_argument('keywords', nargs='+', help='Keywords to search for (e.g. "lidar" "autonomous")')
    parser.add_argument('--assignee', '-a', help='Limit search to a specific company/assignee')
    parser.add_argument('--inventor', '-i', help='Limit search to a specific inventor')
    parser.add_argument('--before', '-b', help='Priority date before (YYYY-MM-DD)')
    parser.add_argument('--after', '-f', help='Priority date after (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    print("\n" + "="*60)
    print("⚔️  PATENT WARRIOR - TACTICAL QUERY GENERATOR ⚔️")
    print("="*60 + "\n")
    
    print(f"[*] Keywords: {', '.join(args.keywords)}")
    if args.assignee: print(f"[*] Target:   {args.assignee}")
    print("-" * 30)
    
    # Google Patents
    gp_url = create_google_patents_url(args.keywords, args.assignee, args.inventor, args.before, args.after)
    print(f"\n[1] GOOGLE PATENTS (Recommended for Speed):\n{gp_url}")
    
    # Espacenet
    en_url = create_espacenet_url(args.keywords)
    print(f"\n[2] ESPACENET (Global Coverage):\n{en_url}")
    
    # USPTO
    uspto_q = create_uspto_url(args.keywords)
    print(f"\n[3] USPTO (Official/Legal):\n{uspto_q}")
    
    print("\n" + "="*60)
    print("TIP: Use 'incognito' mode if doing heavy reconnaissance.")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
