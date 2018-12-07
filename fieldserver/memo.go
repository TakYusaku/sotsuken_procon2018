func StartServer(w http.ResponseWriter, r *http.Request) {
    r.ParseForm()
    prov:=r.Form["init_order"]
    for i:=0; i<4; i++{
      init_order[i], _ =strconv.Atoi(prov[i])
    }

    rand.Seed(time.Now().UnixNano())
    turn=rand.Intn(40)+40
    length=rand.Intn(4)+8
    width=rand.Intn(4)+8
    fmt.Fprintf(w,"%d\n",turn)
    fmt.Fprintf(w,"%d\n",length)
    fmt.Fprintf(w,"%d\n",width)

    if init_order[1]  {

    }
    field=make([][]int,(length+1)/2)
    for i:=0; i<(length+1)/2; i++{
      field[i]=make([]int, width)
      for j:=0; j<width; j++ {
        field[i][j]=rand.Intn(32)-16
        //fmt.Fprintf(w,"%d ",field[i][j])
      }
      //fmt.Fprintf(w,"\n")
    }

    tmp_field:=make([][]int,length/2)
    for i:=0; i<length/2; i++{
      tmp_field[i]=make([]int, width)
      tmp_field[i]=field[((length)/2)-1-i]
    }
    field=append(field,tmp_field...)

    for i:=0; i<length; i++{
      for j:=0; j<width; j++ {
        fmt.Fprintf(w,"%d ",field[i][j])
      }
      fmt.Fprintf(w,"\n")
    }

    //user:=make([][]int,length)
    for i:=0; i<length; i++{
      user[i]=make([]int, width)
    }
/*
    fmt.Fprintf(w,"%d ",width)
    fmt.Fprintf(w,"\n")
    fmt.Fprintf(w,"%d ",width/2-1)
    fmt.Fprintf(w,"\n")
    fmt.Fprintf(w,"%d ",(width/2-1)-2)
    //a:=rand.Intn((width/2-1)-2)+1
    //fmt.Fprintf(w,"%d ",a)
    fmt.Fprintf(w,"\n")
*/
    //p:=make(map[int]map[string]int)
    for i:=1; i<5; i++{
      p[i]=make(map[string]int)
    }
    x:=rand.Intn((width/2-1)-2)+1
    y:=rand.Intn((length/2-1)-2)+1
    p[1]["x"]=x
    p[1]["y"]=y
    p[2]["x"]=x
    p[2]["y"]=width-y-1
    p[3]["x"]=length-x-1
    p[3]["y"]=y
    p[4]["x"]=length-x-1
    p[4]["y"]=width-y-1

    for i:=1; i<5; i++{
      user[p[i]["x"]][p[i]["y"]]=retIndex(i)
    }

/*
    user[x][y]=1
    user[x][width-y-1]=2
    user[length-x-1][y]=3
    user[length-x-1][width-y-1]=4
*/
    for i:=0; i<length; i++{
      for j:=0; j<width; j++ {
        fmt.Fprintf(w,"%d ",user[i][j])
      }
      fmt.Fprintf(w,"\n")
    }

}
