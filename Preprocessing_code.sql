# Handling Missing Values

select * from pallet_masked_fulldata 
where MyUnknownColumn is null
or `Date` is null
or CustName is null
or city is null
or Region is null
or State is null
or `Product Code` is null
or `Transaction Type` is null
or  qty is null
or  WHName is null;


# Removing Duplicates

select distinct MyUnknownColumn,
`Date`, 
CustName, 
City, 
Region, 
State, 
`Product Code`, 
`Transaction Type`, 
QTY, 
WHName
from pallet_masked_fulldata;


# Changing column name
alter table pallet_masked_fulldata
change MyUnknownColumn  `S.No.` int;

alter table pallet_masked_fulldata
change CustName  CustID int;


#Changing column datatype
ALTER TABLE pallet_masked_fulldata
MODIFY COLUMN `Date` DATETIME;


# Handling outliers using Z-Score Method

-- Set Z-score threshold (e.g., 3 standard deviations away from the mean)
SET @z_score_threshold = 3;

-- Identify outliers using Z-score
SELECT QTY
FROM pallet_masked_fulldata
WHERE ABS((QTY - (SELECT AVG(QTY) FROM pallet_masked_fulldata)) / (SELECT STDDEV(QTY) FROM pallet_masked_fulldata)) > @z_score_threshold;







