library (tmap)
library (sf)
library (tidyverse)
data ("World")
tmap_mode("view")

tm_shape(World) + tm_polygons(c("HPI"))
tm_shape(World) + tm_polygons(c("HPI","economy")) + tm_facets(ncol = 2)


spmis <- "/Users/nicholustintzaw/Dropbox/06_DSW_SP_Database/_Union_SP_MIS/_report/formap.csv"

spmis <- read.csv (spmis, stringsAsFactors = F)
spmis_2 <- spmis %>%
  mutate(pcode_sr=replace(pcode_sr, X == 5, 'MMR222')) %>%
  as.data.frame()

spmis_2 <- spmis_2 %>%
  mutate(pcode_sr=replace(pcode_sr, X == 2, 'MMR111')) %>%
  as.data.frame()

spmis$benef_count <- 1
spmis_2$benef_count <- 1


sp.map <- st_read("/Users/nicholustintzaw/Dropbox/06_DSW_SP_Database/00_report_demo/05_shape_files/01_state_region/mmr_polbnda_adm1_mimu_250k.shp", stringsAsFactors = F)

names (sp.map) [3] = "pcode_sr"

final.map = left_join(sp.map, spmis, by = "pcode_sr")


tm_shape(final.map) + tm_polygons("Total.New.Register", id = "ST", popup.vars = c("Total Benef:" = "Total.New.Register"))

tm_shape(final.map) + tm_polygons("total_benef", 
                                  id = "sr_name_dsw", 
                                  popup.vars = c("State/Region Name"="sr_name_dsw", 
                                                 "Total Benef:" = "total_benef",
                                                 "Total Id Duplicate:" = "duplicated_id",
                                                 "Total Personal Info Duplicate (include same id):" = "duplciated_personal_info",
                                                 "Total Personal Info Only Duplicate (exclude same id):" = "duplicated_personal_info_exclude_id",
                                                 "Total Personal Info Duplicate between different regions:" = "duplicated_personal_info_across_region"
                                                 ), alpha = 0.5)


tm_shape(final.map) + tm_polygons("total_benef", 
                                  id = "sr_name_dsw", 
                                  popup.vars = c("State/Region Name"="sr_name_dsw", 
                                                 "Total Benef:" = "total_benef",
                                                 "Id Duplicate:" = "duplicated_id",
                                                 "Personal Info Only Duplicate:" = "duplicated_personal_info_exclude_id"
                                  ), alpha = 0.5)


## vlsilization
spmis %>%
  ggplot(aes(x = total_benef, y = duplicated_id)) + geom_point()



spmis %>%
  mutate(prop = duplicated_id/total_benef) %>%
  mutate(sr_dsw_name_eng = factor(sr_dsw_name_eng, levels = sr_dsw_name_eng[order(prop, decreasing = T)])) %>%
  ggplot(aes(sr_dsw_name_eng, prop)) + geom_bar(stat = "identity") +
  labs(x = "State/Region Names", y = "Id Duplicate Proportion", title = "ID Duplicated rate in SP", caption = "In 4th Qrt 2018-2019 Data") +
  theme(axis.text.x = element_text(angle = 90))


spmis <- spmis %>%
  mutate(prop = duplicated_id/total_benef)

spmis %>%
  ggplot(aes(sr_dsw_name_eng, prop)) +  geom_bar(stat = "identity")





