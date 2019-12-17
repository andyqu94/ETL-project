-- Query to ccheck successful load
SELECT * FROM top40_mining_companies;
SELECT * FROM market_cap;


-- Join tables on top 40 companies' names
SELECT * FROM market_cap
INNER JOIN top40_mining_companies
ON market_cap.company = top40_mining_companies.company