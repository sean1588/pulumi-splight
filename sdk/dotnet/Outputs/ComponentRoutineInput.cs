// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Splight.Splight.Outputs
{

    [OutputType]
    public sealed class ComponentRoutineInput
    {
        public readonly string? Description;
        public readonly bool? Multiple;
        public readonly string Name;
        public readonly bool? Required;
        public readonly bool? Sensitive;
        public readonly string? Type;
        public readonly string? ValueType;
        public readonly ImmutableArray<Outputs.ComponentRoutineInputValue> Values;

        [OutputConstructor]
        private ComponentRoutineInput(
            string? description,

            bool? multiple,

            string name,

            bool? required,

            bool? sensitive,

            string? type,

            string? valueType,

            ImmutableArray<Outputs.ComponentRoutineInputValue> values)
        {
            Description = description;
            Multiple = multiple;
            Name = name;
            Required = required;
            Sensitive = sensitive;
            Type = type;
            ValueType = valueType;
            Values = values;
        }
    }
}
