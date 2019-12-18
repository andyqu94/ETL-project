CREATE TABLE top40_mining_companies (
	id INT PRIMARY KEY,
	Company TEXT,
	Revenue_Million TEXT
);

CREATE TABLE market_cap (
	id INT PRIMARY KEY,
	Company TEXT,
	QMV_C$ TEXT,
	OS_Shares TEXT,
	HQ_Location TEXT,
	Volume_YTD TEXT,
	Value_C$_YTD TEXT,
	Number_of_Trades_YTD TEXT
)

		