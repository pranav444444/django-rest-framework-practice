import django_filters
from.models import Employee


class EmployeeFilter(django_filters.FilterSet):
  designation=django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
  #'iexact' will also accpet case sensitive expressions.. for example "Data Scientist" and "data scientisi"... it will accpet both for filteting
  
  #now lets extract all the employyes who have John in their names
  emp_name=django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains')
  
  #now lets get employee id between emp002 and emp006
  #Range filter only works on integer or primary key and emp_id is Char field.
  #so we wrote 'id' insread of 'emp_id' as it is  a priamry key
  # id=django_filters.RangeFilter(field_name='id') #pls note this is primary key id not "emp_id"
  

  #Now we will writwe the code to get range for 'emp_id' too
  id_min=django_filters.CharFilter(method='filter_by_id_range',label='From EMP ID')
  id_max=django_filters.CharFilter(method='filter_by_id_range',label = 'To EMP ID')
  
  
  class  Meta:
    model=Employee
    fields=['designation','emp_name','id_min','id_max']
    
  def filter_by_id_range(self,queryset,name,value):#queryset=table,name=field names,values=rows
    if name == 'id_min':
      return queryset.filter(emp_id__gte=value) #gte=greater than or equal to
    elif name == 'id_max':
      return queryset.filter(emp_id__lte=value) #lte=less than or equal to
    return queryset
    
    
