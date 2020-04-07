library('ggplot2')
df<-read.delim('../outputdir/DataforR',header=T)
df$BpSite<-df$Site+df$RelaBpSite
lt<-table(df$BpSite)
lt2<-as.data.frame(lt)
pdf('../outputdir/PiedBpSites.pdf',height=6,width=12)
ggplot(df)+geom_bar(aes(x=BpSite),alpha=10)+geom_point(data=lt2,aes(x=Var1,y=Freq))+scale_x_discrete(limits=1:30000,breaks=c(5000,10000,15000,20000,25000,30000))+geom_segment(x=21552,xend=21552,y=0,yend=-25,colour='red')+geom_segment(x=25382,xend=25382,y=0,yend=-25,colour='red')+geom_segment(x=26237,xend=26237,y=0,yend=-25,colour='red')+geom_segment(x=26468,xend=26468,y=0,yend=-25,colour='red')+geom_segment(x=27041,xend=27041,y=0,yend=-25,colour='red')+geom_segment(x=27385,xend=27385,y=0,yend=-25,colour='red')+geom_segment(x=27483,xend=27483,y=0,yend=-25,colour='red')+geom_segment(x=27884,xend=27884,y=0,yend=-25,colour='red')+geom_segment(x=28255,xend=28255,y=0,yend=-25,colour='red')+geom_segment(x=68,xend=68,y=0,yend=-25,colour='red')
dev.off()
